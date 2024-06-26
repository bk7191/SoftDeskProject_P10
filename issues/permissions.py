from rest_framework import permissions
from rest_framework.permissions import BasePermission

import projects
from .models import Issue
from projects.models import Contributor
