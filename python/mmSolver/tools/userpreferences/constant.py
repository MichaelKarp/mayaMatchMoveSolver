# Copyright (C) 2020 David Cattermole.
#
# This file is part of mmSolver.
#
# mmSolver is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# mmSolver is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with mmSolver.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Contains constant data to be used for user preferences.
"""

CONFIG_FILE_NAME = 'user_preferences.json'

# "Register Events - Add New Markers To" preference.
REG_EVNT_ADD_NEW_MKR_TO_KEY = 'register_events/add_new_markers_to'
REG_EVNT_ADD_NEW_MKR_TO_NONE_VALUE = 0
REG_EVNT_ADD_NEW_MKR_TO_NONE_LABEL = 'None'
REG_EVNT_ADD_NEW_MKR_TO_ACTIVE_COL_VALUE = 1
REG_EVNT_ADD_NEW_MKR_TO_ACTIVE_COL_LABEL = 'Active Collection'
REG_EVNT_ADD_NEW_MKR_TO_VALUES = [
    REG_EVNT_ADD_NEW_MKR_TO_NONE_VALUE,
    REG_EVNT_ADD_NEW_MKR_TO_ACTIVE_COL_VALUE,
]
REG_EVNT_ADD_NEW_MKR_TO_LABELS = [
    REG_EVNT_ADD_NEW_MKR_TO_NONE_LABEL,
    REG_EVNT_ADD_NEW_MKR_TO_ACTIVE_COL_LABEL,
]


# "Solver UI - Validate on open" preference.
SOLVER_UI_VALIDATE_ON_OPEN_KEY = 'solver_ui/validate_on_open'
SOLVER_UI_VALIDATE_ON_OPEN_TRUE_VALUE = 1
SOLVER_UI_VALIDATE_ON_OPEN_TRUE_LABEL = 'Yes'
SOLVER_UI_VALIDATE_ON_OPEN_FALSE_VALUE = 0
SOLVER_UI_VALIDATE_ON_OPEN_FALSE_LABEL = 'No'
SOLVER_UI_VALIDATE_ON_OPEN_VALUES = [
    SOLVER_UI_VALIDATE_ON_OPEN_TRUE_VALUE,
    SOLVER_UI_VALIDATE_ON_OPEN_FALSE_VALUE,
]
SOLVER_UI_VALIDATE_ON_OPEN_LABELS = [
    SOLVER_UI_VALIDATE_ON_OPEN_TRUE_LABEL,
    SOLVER_UI_VALIDATE_ON_OPEN_FALSE_LABEL,
]


# "Solver UI - Show Validate Button" preference.
SOLVER_UI_SHOW_VALIDATE_BTN_KEY = 'solver_ui/show_validate_button'
SOLVER_UI_SHOW_VALIDATE_BTN_TRUE_VALUE = 1
SOLVER_UI_SHOW_VALIDATE_BTN_TRUE_LABEL = 'Yes'
SOLVER_UI_SHOW_VALIDATE_BTN_FALSE_VALUE = 0
SOLVER_UI_SHOW_VALIDATE_BTN_FALSE_LABEL = 'No'
SOLVER_UI_SHOW_VALIDATE_BTN_VALUES = [
    SOLVER_UI_SHOW_VALIDATE_BTN_TRUE_VALUE,
    SOLVER_UI_SHOW_VALIDATE_BTN_FALSE_VALUE,
]
SOLVER_UI_SHOW_VALIDATE_BTN_LABELS = [
    SOLVER_UI_SHOW_VALIDATE_BTN_TRUE_LABEL,
    SOLVER_UI_SHOW_VALIDATE_BTN_FALSE_LABEL,
]


# Key to Values mapping.
VALUES_MAP = {
    REG_EVNT_ADD_NEW_MKR_TO_KEY: REG_EVNT_ADD_NEW_MKR_TO_VALUES,
    SOLVER_UI_VALIDATE_ON_OPEN_KEY: SOLVER_UI_VALIDATE_ON_OPEN_VALUES,
    SOLVER_UI_SHOW_VALIDATE_BTN_KEY: SOLVER_UI_SHOW_VALIDATE_BTN_VALUES,
}


# Key to Labels mapping.
LABELS_MAP = {
    REG_EVNT_ADD_NEW_MKR_TO_KEY: REG_EVNT_ADD_NEW_MKR_TO_LABELS,
    SOLVER_UI_VALIDATE_ON_OPEN_KEY: SOLVER_UI_VALIDATE_ON_OPEN_LABELS,
    SOLVER_UI_SHOW_VALIDATE_BTN_KEY: SOLVER_UI_SHOW_VALIDATE_BTN_LABELS,
}


# Key to default values.
DEFAULT_VALUE_MAP = {
    REG_EVNT_ADD_NEW_MKR_TO_KEY: REG_EVNT_ADD_NEW_MKR_TO_ACTIVE_COL_VALUE,
    SOLVER_UI_VALIDATE_ON_OPEN_KEY: SOLVER_UI_VALIDATE_ON_OPEN_FALSE_VALUE,
    SOLVER_UI_SHOW_VALIDATE_BTN_KEY: SOLVER_UI_SHOW_VALIDATE_BTN_FALSE_VALUE,
}

# A list of all the valid keys in the user preferences file.
VALID_KEYS = DEFAULT_VALUE_MAP.keys()
