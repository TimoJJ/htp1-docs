# Updates and Support

## Checking Your Version

Open [System Status](system-status.md) to see the software version currently installed and whether
a newer release is available.

Click **Check for updates** to refresh the information. If the release server is unreachable, the
page explains the problem and may show information from the last successful check.

## Version History

Click **Version history** on the System Status page to see available software releases.

Version history lists available firmware versions, release dates, release notes, and installation
options. Enable **Show release candidates and betas** to include versions that are still being tested.
These may contain new features and fixes but are not yet final releases.

## Installing an Update

Select the version you want to install and click **Install**. You can also reinstall the currently
installed version or return to an older version listed in Version history.

Review the release notes before installing, then confirm your selection.

Version history is also accessible while the HTP-1 is in standby through
**View version history and install updates**.

!!! tip
    Export your configuration before updating. See [Backup and Restore](configs.md).
    Configuration exports do not include Dirac Live filter files.

## What to Expect

During installation, the web interface displays progress messages and a progress bar. Installation
may take several minutes. Do not disconnect power while the update is running.

The HTP-1 restarts automatically when installation finishes. Open browser tabs reconnect and reload
when the unit becomes available again.

During startup, you may see **HTP-1 is starting** or **Preparing Dirac Live filters**.

The first startup after updating may take longer because the HTP-1 checks its stored Dirac Live
filters and prepares missing filter versions.

Your existing settings and calibrations are preserved during a normal firmware update.

## Upgrading from Version 1.x

Moving from the version 1.x software to the version 2 software is a one-time procedure with a few
extra steps. The update backs up your existing system so you can roll back, but take your own
backup first if you have spent time configuring the unit.

Export your settings from the [Backup and Restore](configs.md) page before you begin. You can also
export your existing Dirac Live filters from that page as an extra copy. Those exports are in the
older filter format and cannot be loaded into the new system, but they are worth keeping.

![Configs page showing the export and import controls](images/art-p05-1.png)

Then perform the update in two stages:

1. Open **History and Updates** from the [System Status](system-status.md) page. It can take a few
   moments for the list to appear. If it times out the first time, try again.
2. Install the release labeled **final non-ART build** first. This creates the backup files that let
   you revert later.
3. When that finishes, a new release supporting Dirac Live ART becomes available. Install it.

Your existing Dirac Live filters are preserved, and you can revert to the earlier software if you
need to.

### Your First Calibration Afterward

No Dirac Live filters are loaded when the new software starts for the first time. To be sure the
unit begins in a consistent state, change the speaker layout twice before calibrating: select a
layout you do not intend to use, then switch to the layout you want to calibrate. Preparing an
unused layout takes about 30 seconds. This is only needed once.

!!! tip
    Each time you change the speaker layout, the filter cache is cleared and reloaded for the new
    layout. With large speaker configurations this takes a while — loading six filters for a 7.3.6
    layout can take up to 10 minutes. If you want to compare layouts, keep one or two calibrations
    per layout to reduce the wait.

## Support

### Downloading Logs

Open **Device Settings**, then the **Danger Zone** section, and click **Download Logs**. This
downloads `quicklogs.zip`, a set of logs useful for troubleshooting. It does not contain any
personally identifiable information.

Send this file along when you report a problem — it gives the development team the detail needed
to reproduce and diagnose it.

### Community Discussion

Much of the HTP-1 owners' discussion about setup, troubleshooting, features, and software updates
takes place in the
[AVS Forum HTP-1 owners thread](https://www.avsforum.com/threads/the-official-monoprice-monolith-htp-1-owners-thread.3112176/).
You can also find this link under **Discussion** on the [System Status](system-status.md) page.

### On-Device Help

Click the **?** icon to open Help for the current page in a side panel without leaving your
settings.

To browse all available Help topics, select **Help** in the settings sidebar. The online User Manual
provides more detailed explanations.
