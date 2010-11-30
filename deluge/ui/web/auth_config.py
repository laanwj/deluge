# -*- coding: utf-8 -*-
AUTH_LEVEL_NONE = 0
AUTH_LEVEL_READONLY = 1
AUTH_LEVEL_NORMAL = 5
AUTH_LEVEL_ADMIN = 10

remote_methods_access = {
    # everyone can get config
    'core.get_config': AUTH_LEVEL_NORMAL,
    'core.get_config_values': AUTH_LEVEL_NORMAL,

    # Changing configuration is special
    # and will be filtered with the table below.
    'core.set_config': AUTH_LEVEL_NORMAL,

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

remote_config_access = {
# not mentioned defaults to AUTH_LEVEL_ADMIN
  "info_sent": AUTH_LEVEL_NORMAL,
  "lsd": AUTH_LEVEL_NORMAL,
  "max_download_speed": AUTH_LEVEL_NORMAL,
  "send_info": AUTH_LEVEL_NORMAL,
  "natpmp": AUTH_LEVEL_NORMAL,
  "move_completed_path": AUTH_LEVEL_ADMIN,
  "peer_tos": AUTH_LEVEL_NORMAL,
  "enc_in_policy": AUTH_LEVEL_NORMAL,
  "queue_new_to_top": AUTH_LEVEL_NORMAL,
  "ignore_limits_on_local_network": AUTH_LEVEL_NORMAL,
  "rate_limit_ip_overhead": AUTH_LEVEL_NORMAL,
  "daemon_port": AUTH_LEVEL_ADMIN,
  "torrentfiles_location": AUTH_LEVEL_ADMIN,
  "max_active_limit": AUTH_LEVEL_NORMAL,
  "geoip_db_location": AUTH_LEVEL_ADMIN,
  "upnp": AUTH_LEVEL_NORMAL,
  "utpex": AUTH_LEVEL_NORMAL,
  "max_active_downloading": AUTH_LEVEL_NORMAL,
  "max_active_seeding": AUTH_LEVEL_NORMAL,
  "allow_remote": AUTH_LEVEL_NORMAL,
  "outgoing_ports": AUTH_LEVEL_NORMAL,
  "enabled_plugins": AUTH_LEVEL_NORMAL,
  "max_half_open_connections": AUTH_LEVEL_NORMAL,
  "download_location": AUTH_LEVEL_ADMIN,
  "compact_allocation": AUTH_LEVEL_NORMAL,
  "max_upload_speed": AUTH_LEVEL_ADMIN,
  "plugins_location": AUTH_LEVEL_ADMIN,
  "max_connections_global": AUTH_LEVEL_NORMAL,
  "enc_prefer_rc4": AUTH_LEVEL_NORMAL,
  "cache_expiry": AUTH_LEVEL_NORMAL,
  "dht": AUTH_LEVEL_NORMAL,
  "stop_seed_at_ratio": AUTH_LEVEL_NORMAL,
  "stop_seed_ratio": AUTH_LEVEL_NORMAL,
  "max_download_speed_per_torrent": AUTH_LEVEL_NORMAL,
  "prioritize_first_last_pieces": AUTH_LEVEL_NORMAL,
  "max_upload_speed_per_torrent": AUTH_LEVEL_NORMAL,
  "auto_managed": AUTH_LEVEL_NORMAL,
  "enc_level": AUTH_LEVEL_NORMAL,
  "copy_torrent_file": AUTH_LEVEL_NORMAL,
  "max_connections_per_second": AUTH_LEVEL_NORMAL,
  "listen_ports": AUTH_LEVEL_NORMAL,
  "max_connections_per_torrent": AUTH_LEVEL_NORMAL,
  "del_copy_torrent_file": AUTH_LEVEL_NORMAL,
  "move_completed": AUTH_LEVEL_ADMIN,
  "autoadd_enable": AUTH_LEVEL_NORMAL,
  "proxies": AUTH_LEVEL_NORMAL,
  "dont_count_slow_torrents": AUTH_LEVEL_NORMAL,
  "add_paused": AUTH_LEVEL_NORMAL,
  "random_outgoing_ports": AUTH_LEVEL_NORMAL,
  "max_upload_slots_per_torrent": AUTH_LEVEL_NORMAL,
  "new_release_check": AUTH_LEVEL_ADMIN,
  "enc_out_policy": AUTH_LEVEL_NORMAL,
  "seed_time_ratio_limit": AUTH_LEVEL_NORMAL,
  "remove_seed_at_ratio": AUTH_LEVEL_NORMAL,
  "autoadd_location": AUTH_LEVEL_ADMIN,
  "max_upload_slots_global": AUTH_LEVEL_NORMAL,
  "seed_time_limit": AUTH_LEVEL_NORMAL,
  "cache_size": AUTH_LEVEL_NORMAL,
  "share_ratio_limit": AUTH_LEVEL_NORMAL,
  "random_port": AUTH_LEVEL_NORMAL,
  "listen_interface": AUTH_LEVEL_ADMIN
}
