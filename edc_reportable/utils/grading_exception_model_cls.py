from __future__ import annotations

from typing import TYPE_CHECKING, Type

from django.apps import apps as django_apps

if TYPE_CHECKING:
    from ..models import GradingException

__all__ = ["grading_exception_model_cls"]


def grading_exception_model_cls() -> Type[GradingException]:
    return django_apps.get_model("edc_reportable.gradingexception")
