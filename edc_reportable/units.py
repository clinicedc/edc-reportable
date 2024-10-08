from django.utils.safestring import mark_safe

CELLS_PER_MICROLITER = "cells/μL"
CELLS_PER_MILLIMETER_CUBED = "cells/mm^3"
CELLS_PER_MILLIMETER_CUBED_DISPLAY = mark_safe("cells/mm<sup>3</sup>")  # nosec B308
COPIES_PER_MILLILITER = "copies/mL"
EGFR_UNITS = "mL/min/1.73m2"
FEMTOLITERS_PER_CELL = "fL/cell"
GRAMS_PER_DECILITER = "g/dL"
GRAMS_PER_LITER = "g/L"
IU_LITER = "IU/L"
IU_LITER_DISPLAY = mark_safe("IU/L")  # nosec B308
MILLI_IU_LITER = "mIU/L"
MILLI_IU_LITER_DISPLAY = mark_safe("mIU/L")  # nosec B308
MICRO_IU_MILLILITER = "uIU/mL"
MICRO_IU_MILLILITER_DISPLAY = mark_safe("μIU/mL")  # nosec B308
MICROMOLES_PER_LITER = "umol/L"
MICROMOLES_PER_LITER_DISPLAY = "μmol/L (micromoles/L)"
MILLIGRAMS_PER_DECILITER = "mg/dL"
MILLIGRAMS_PER_LITER = "mg/L"
MILLILITER_PER_MINUTE = "mL/min"
MILLIMOLES_PER_LITER = "mmol/L"
MILLIMOLES_PER_LITER_DISPLAY = "mmol/L (millimoles/L)"
MM3 = "mm3"
MM3_DISPLAY = mark_safe("mm<sup>3</sup>")  # nosec B308
PERCENT = "%"
PICOGRAMS_PER_CELL = "pg/cell"
PLUS = "+"
TEN_X_3_PER_LITER = "10^3/L"
TEN_X_3_PER_LITER_DISPLAY = mark_safe("10<sup>3</sup>/L")  # nosec B308
TEN_X_9_PER_LITER = "10^9/L"
TEN_X_9_PER_LITER_DISPLAY = mark_safe("10<sup>9</sup>/L")  # nosec B308
