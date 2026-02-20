---
title: Backup API | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/apis/subsystems/backup
source: sitemap
fetched_at: 2026-02-17T15:03:53.902636-03:00
rendered_js: false
word_count: 1061
summary: This document explains how to implement the Moodle Backup API to include custom plugin data in course backups using specialized task and step classes.
tags:
    - moodle
    - backup-api
    - plugin-development
    - activity-modules
    - php
    - backup-task
category: api
---

The Backup API provides a way to include your plugin's in the course backup. See [Restore API](https://moodledev.io/docs/4.4/apis/subsystems/backup/restore) for the part that takes care of restoring data.

## Overview[​](#overview "Direct link to Overview")

This page provides just a quick reference to the backup machinery in Moodle 2.0 and higher. There is a detailed documentation available at [Backup 2.0](https://docs.moodle.org/dev/Backup_2.0) page - see especially the tutorial for plugin authors at [Backup 2.0 for developers](https://docs.moodle.org/dev/Backup_2.0_for_developers) page.

Moodle creates backups of courses or their parts by executing so called *backup plan*. The backup plan consists of a set of *backup tasks* and finally each backup task consists of one or more *backup steps*. You as the developer of a plugin will have to implement one backup task that deals with your plugin data. Most plugins have their backup tasks consisting of a single backup step - the one that creates the XML file with data from your plugin's tables. Some activities may need two or more steps to finish their backup task though (for example the backup task of the Quiz module consists of three steps as it needs to write not just the Quiz setting itself but also the questions used by that particular quiz).

There are subtle differences in how the backup code is organised in various supported plugin types (activity modules, blocks, themes, course reports).

## API for activity modules[​](#api-for-activity-modules "Direct link to API for activity modules")

### Files[​](#files "Direct link to Files")

The files that implement the backup support in your activity module must be located in the subdirectory backup/moodle2/ in your plugin's folder. So, if you are developing the activity module called *foobar* then the backup files will be located in mod/foobar/backup/moodle2/ folder.

The following two files are supposed to exist in that location (replace *foobar* with the name of your module):

- **backup\_foobar\_activity\_task.class.php**  
  Provides the activity task class
- **backup\_foobar\_stepslib.php**  
  Provides all the backup steps classes

If your module declares its own backup setting (apart from the ones common for all activity modules provided by the core), you will also want to create the backup\_foobar\_settingslib.php file to provide the setting classes. However most modules do not need this feature.

### Backup task class[​](#backup-task-class "Direct link to Backup task class")

The file backup\_foobar\_activity\_task.class.php must provide a single class called **backup\_foobar\_activity\_task**. All activity tasks extend the backup\_activity\_task class.

There are three methods that your class must define.

- **protected function define\_my\_settings()**  
  If your module declares own backup settings defined in the file backup\_foobar\_settingslib.php, add them here. Most modules just leave the method body empty.
- **protected function define\_my\_steps()**  
  This method typically consists of one or more `$this->add_step()` calls. This is the place where you define the task as a sequence of steps to execute.
- **static public function encode\_content\_links($content)**  
  The current instance of the activity may be referenced from other places in the course by URLs like `http://my.moodle.site/mod/foobar/view.php?id=42` Obviously, such URLs are not valid any more once the course is restored elsewhere. For this reason the backup file does not store the original URLs but encodes them into a transportable form. During the restore, the reverse process is applied and the encoded URLs are replaced with the new ones valid for the target site.

### Backup structure step class[​](#backup-structure-step-class "Direct link to Backup structure step class")

The classes that represent the backup steps added in define\_my\_steps() are implemented in the file backup\_foobar\_stepslib.php. Most plugins define just a single step in the class called **backup\_foobar\_activity\_structure\_step** that extends the backup\_activity\_structure\_step class. This class defines the structure step - that is the step where the structure of your plugin's instance data is described and linked with the data sources.

You have to implement a single method `protected function define_structure()` in this class class. There are three main things that the method must do.

- Create a set of backup\_nested\_element instances that describe the required data of your plugin
- Connect these instances into a hierarchy using their `add_child()` method
- Set data sources for the elements, using their methods like `set_source_table()` or `set_source_sql()`

The method must return the root backup\_nested\_element instance processed by the `prepare_activity_structure()` method (which just wraps your structures with a common envelope).

## API for blocks[​](#api-for-blocks "Direct link to API for blocks")

### Files[​](#files-1 "Direct link to Files")

The files that implement the backup support in your block must be located in the subdirectory backup/moodle2/ in your plugin's folder. So, if you are developing the block called *foobar* then the backup files will be located in blocks/foobar/backup/moodle2/ folder.

At least the file backup\_foobar\_block\_task.class.php is supposed to exist in that location (replace *foobar* with the name of your block).

If your block defines its own database tables, data from which must be included in the backup, you will want to create a file backup\_foobar\_stepslib.php, too. Additionally, if your block declares its own backup setting, you will also want to create the backup\_foobar\_settingslib.php file to provide the setting classes. However most blocks do not need this feature.

### Backup task class[​](#backup-task-class-1 "Direct link to Backup task class")

The file backup\_foobar\_block\_task.class.php must provide a single class called **backup\_foobar\_block\_task**. All block tasks extend the backup\_block\_task class.

There are five methods that your class must define.

- **protected function define\_my\_settings()**  
  If your block declares own backup settings defined in the file backup\_foobar\_settingslib.php, add them here. Most blocks just leave the method body empty.
- **protected function define\_my\_steps()**  
  Blocks that do not have their own database tables usually leave this method empty. Otherwise this method consists of one or more `$this->add_step()` calls where you define the task as a sequence of steps to execute.
- **public function get\_fileareas()**  
  Returns the array of file area names within the block context.
- **public function get\_configdata\_encoded\_attributes()**  
  Instead of using their own tables, blocks usually use the configuration tables to hold their data (see the instance\_config\_save() of the block class). This method returns the array of all config elements that must be processed before they are stored in the backup. This is typically used when the stored config elements holds links to embedded media. Most blocks just return empty array here.
- **static public function encode\_content\_links($content)**  
  If the current instance of the block may be referenced from other places in the course by URLs, it must be encoded into a transportable form. Most blocks just return unmodified $content parameter.

The files that implement the backup support in your plugin must be located in the subdirectory *backup/moodle2/* in your plugin's folder. So, if you are developing *tool\_foobar* then the backup files will be located in *admin/tool/foobar/backup/moodle2/*.

### Task class[​](#task-class "Direct link to Task class")

The file backup\_tool\_foobar\_plugin.class.php must provide a single class called *backup\_tool\_foobar\_task* extending *backup\_tool\_plugin*.

Here is a minimalistic task:

```
require_once($CFG->dirroot.'/backup/moodle2/backup_tool_plugin.class.php');

classbackup_tool_foobar_pluginextendsbackup_tool_plugin{

protectedfunctiondefine_course_plugin_structure(){
$this->step->log('Yay, backup!',backup::LOG_DEBUG);
return$plugin;
}

}
```

## API for themes[​](#api-for-themes "Direct link to API for themes")

See [Backup 2.0 theme data](https://docs.moodle.org/dev/Backup_2.0_theme_data)

## API for reports[​](#api-for-reports "Direct link to API for reports")

See [Backup 2.0 course report data](https://docs.moodle.org/dev/Backup_2.0_course_report_data)

## See also[​](#see-also "Direct link to See also")

- [Restore API](https://moodledev.io/docs/4.4/apis/subsystems/backup/restore)
- [Core APIs](https://moodledev.io/docs/4.4/apis)