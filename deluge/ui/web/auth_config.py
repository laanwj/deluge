# -*- coding: utf-8 -*-
AUTH_LEVEL_NONE = 0
AUTH_LEVEL_READONLY = 1
AUTH_LEVEL_NORMAL = 5
AUTH_LEVEL_ADMIN = 10

remote_methods_access = {
    # everyone can get config
    'core.get_config': AUTH_LEVEL_NORMAL,
    'core.get_config_values': AUTH_LEVEL_NORMAL,

    # Changing configuration is admin only
    'core.set_config': AUTH_LEVEL_ADMIN,

    # Moving files as well
    'core.move_storage': AUTH_LEVEL_ADMIN,
    # Same for plugin ops
    'core.disable_plugin': AUTH_LEVEL_ADMIN,
    'core.enable_plugin': AUTH_LEVEL_ADMIN,

    # Torrent manipulation is for everyone
    'core.remove_torrent': AUTH_LEVEL_NORMAL,
    'core.force_reannounce': AUTH_LEVEL_NORMAL,
    'core.force_recheck': AUTH_LEVEL_NORMAL,
    'core.set_torrent_prioritize_first_last': AUTH_LEVEL_NORMAL,
    'core.set_torrent_options': AUTH_LEVEL_NORMAL,
    'core.set_torrent_file_priorities': AUTH_LEVEL_NORMAL,
    'core.set_torrent_trackers': AUTH_LEVEL_NORMAL,
    'core.get_torrent_status': AUTH_LEVEL_NORMAL,
}
