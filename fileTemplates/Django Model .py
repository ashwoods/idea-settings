# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from guardian.shortcuts import assign
from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager

