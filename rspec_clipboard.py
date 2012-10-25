import sublime
import sublime_plugin
import os

class CopyRspecWithLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    command = get_rspec_command(self.view)
    line_number = self.view.rowcol(self.view.sel()[0].begin())[0]
    command += ":" + str(line_number)
    sublime.set_clipboard(command)

class CopyRspecCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    command = get_rspec_command(self.view)
    sublime.set_clipboard(command)

def get_rspec_command(view):
  file_name = view.file_name()
  folders = sublime.active_window().folders()

  for folder in folders:
    index = file_name.find(folder)
    if index >= 0:
      file_name = file_name[len(folder) + 1:]
      break

  return "rspec " + file_name
