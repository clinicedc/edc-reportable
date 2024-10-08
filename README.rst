|pypi| |actions| |codecov|

edc-reportable
--------------

Reportable clinic events, reference ranges, grading

.. code-block:: python

    from dateutil.relativedelta import relativedelta
    from edc_utils import get_utcnow
    from edc_constants.constants import MALE, FEMALE
    from edc_reportable import ValueReferenceGroup, NormalReference, GradeReference
    from edc_reportable import site_reportables
    from edc_reportable.tests.reportables import normal_data, grading_data

Create a group for each test:

.. code-block:: python

    neutrophils = ValueReferenceGroup(name='neutrophils')

A normal reference is declared like this:

.. code-block:: python

    ref = NormalReference(
        name='neutrophils',
        lower=2.5,
        upper=7.5,
        units='10e9/L',
        age_lower=18,
        age_upper=99,
        age_units='years',
        gender=[MALE, FEMALE])

    >>> ref
    NormalReference(neutrophils, 2.5<x<7.5 10e9/L MF, 18<AGE<99 years)

And added to a group like this:

.. code-block:: python

    neutrophils.add_normal(ref)

Add as many normal references in a group as you like, just ensure the ``lower`` and ``upper`` boundaries don't overlap.

 **Note**: If the lower and upper values of a normal reference overlap
 with another normal reference in the same group, a ``BoundaryOverlap``
 exception will be raised when the value is evaluated.
 Catch this in your tests.

A grading reference is declared like this:

.. code-block:: python

    g3 = GradeReference(
        name='neutrophils',
        grade=3,
        lower=0.4,
        lower_inclusive=True,
        upper=0.59,
        upper_inclusive=True,
        units='10e9/L',
        age_lower=18,
        age_upper=99,
        age_units='years',
        gender=[MALE, FEMALE])

    >>> g3
    GradeReference(neutrophils, 0.4<=x<=0.59 in 10e9/L GRADE 3, MF, 18<AGE<99 in years) GRADE 3)

    or using lower / upper limits of normal:

    g3 = GradeReference(
        name="amylase",
        grade=1,
        lower="3.0*ULN",
        upper="5.0*ULN",
        lower_inclusive=True,
        upper_inclusive=False,
        units=IU_LITER,
        gender=MALE,
        normal_references={MALE: [normal_reference]},
        **adult_age_options)

    >>> g3
    GradeReference(amylase, 375.0<=x<625.0 IU/L GRADE 3) GRADE 3)

And added to the group like this:

.. code-block:: python

    neutrophils.add_grading(g3)

Declare and add a ``GradeReference`` for each reportable grade of the test.

 **Note**: If the lower and upper values of a grade reference overlap
 with another grade reference in the same group, a ``BoundaryOverlap``
 exception will be raised when the value is evaluated.
 Catch this in your tests.


Declaring with ``parse``
========================

You may find using ``parse`` somewhat simplifies the declaration where ``lower``, ``lower_inclusive``, ``upper`` and ``upper_inclusive`` can be written as a phrase, like ``13.5<=x<=17.5``. For example:

.. code-block:: python

    age_opts = dict(
        age_lower=18,
        age_upper=120,
        age_units='years',
        age_lower_inclusive=True,
        age_upper_inclusive=True)

    normal_data = {
        'haemoglobin': [
            p('13.5<=x<=17.5', units=GRAMS_PER_DECILITER,
              gender=[MALE], **age_opts),
            p('12.0<=x<=15.5', units=GRAMS_PER_DECILITER, gender=[FEMALE], **age_opts)],
         ...
    }


Registering with ``site_reportables``
=====================================

Once you have declared all your references, register them

.. code-block:: python

    site_reportables.register(
        name='my_project',
        normal_data=normal_data,
        grading_data=grading_data)



**Important**:
 Writing out references is prone to error. It is better to declare a
 dictionary of normal references and grading references. Use the ``parse`` function
 so that you can use a phrase like ``13.5<=x<=17.5`` instead of a listing attributes.
 There are examples of complete ``normal_data`` and ``grading_data`` in the tests.
 See``edc_reportable.tests.reportables``.

Attempting to grade a value without grading data
++++++++++++++++++++++++++++++++++++++++++++++++
If a value is pased to the evaluator and no grading data exists in the reference lists for
that test, an exception is raised.

Limiting what is "gradeable" for your project
+++++++++++++++++++++++++++++++++++++++++++++
The default tables have grading data for grades 1-4. The evaluator will grade any value
if there is grading data. You can prevent the evaluator from considering grades by passing
``reportable_grades`` when you register the normal and grading data.

For example:

.. code-block:: python

    site_reportables.register(
        name='my_project',
        normal_data=normal_data,
        grading_data=grading_data,
        reportable_grades=[GRADE3, GRADE4],
    )

In the above, by explicitly passing a list of grades, the evaluator will only raise an
exception for grades 3 and 4. If a value meets the criteria for grade 1 or 2, it will be ignored.

Declaring minor exceptions
++++++++++++++++++++++++++

Minor exceptions can be specified using the parameter ``reportable_grades_exceptions``.
For example, you wish to report grades 2,3,4 for Serum Amylase
but grades 3,4 for everything else. You would register as follows:

.. code-block:: python

    site_reportables.register(
        name='my_project',
        normal_data=normal_data,
        grading_data=grading_data,
        reportable_grades=[GRADE3, GRADE4],
        reportable_grades_exceptions={"amylase": [GRADE2, GRADE3, GRADE4]}
    )



Exporting the reference tables
++++++++++++++++++++++++++++++

You can export your declared references to CSV for further inspection

.. code-block:: python

    >>> site_reportables.to_csv(name='my_project', path='~/')

    ('/Users/erikvw/my_project_normal_ranges.csv',
    '/Users/erikvw/my_project_grading.csv')

Using your reportables
======================

In your code, get the references by collection name:

.. code-block:: python

    my_project_reportables = site_reportables.get('my_project')

    neutrophil = my_project_reportables.get('neutrophil')

    report_datetime = get_utcnow()
    dob = (report_datetime - relativedelta(years=25)).date()

Check a normal value
====================

If a value is normal, ``get_normal`` returns the ``NormalReference`` instance that matched with the value.

.. code-block:: python

    # evaluate a normal value
    normal = neutrophil.get_normal(
        value=3.5, units='10^9/L',
        gender=MALE, dob=dob, report_datetime=report_datetime)

    # returns a normal object with information about the range selected
    >>> normal.description
    '2.5<=3.5<=7.5 10^9/L MF, 18<=AGE years'

Check an abnormal value
=======================

If a value is abnormal, ``get_normal`` returns ``None``.

.. code-block:: python

    # evaluate an abnormal value
    opts = dict(
        units='10^9/L',
        gender=MALE, dob=dob,
        report_datetime=report_datetime)
    normal = neutrophil.get_normal(value=0.3, **opts)

    # returns None
    >>> if not normal:
            print('abnormal')
    'abnormal'

To show which ranges the value was evaluated against

.. code-block:: python

    # use same options for units, gender, dob, report_datetime
    >>> neutrophil.get_normal_description(**opts)
    ['2.5<=x<=7.5 10^9/L MF, 18<=AGE years']

Check if a value is "reportable"
================================

.. code-block:: python

    grade = neutrophil.get_grade(
        value=0.43, units='10^9/L',
        gender=MALE, dob=dob, report_datetime=report_datetime)

    >>> grade.grade
    3

    >>> grade.description
    '0.4<=0.43<=0.59 10^9/L GRADE 3'

    grade = neutrophil.get_grade(
        value=0.3, units='10^9/L',
        gender=MALE, dob=dob, report_datetime=report_datetime)

    >>> grade.grade
    4

    >>> grade.description
    '0.3<0.4 10^9/L GRADE 4'

If the value is not evaluated against any reportable ranges, a ``NotEvaluated`` exception is raised

.. code-block:: python

    # call with the wrong units

    >>> grade = neutrophil.get_grade(
            value=0.3, units='mmol/L',
            gender=MALE, dob=dob, report_datetime=report_datetime)

        NotEvaluated: neutrophil value not graded. No reference range found ...

.. |pypi| image:: https://img.shields.io/pypi/v/edc-reportable.svg
    :target: https://pypi.python.org/pypi/edc-reportable

.. |actions| image:: https://github.com/clinicedc/edc-reportable/actions/workflows/build.yml/badge.svg
  :target: https://github.com/clinicedc/edc-reportable/actions/workflows/build.yml

.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-reportable/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/clinicedc/edc-reportable
