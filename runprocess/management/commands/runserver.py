import os
from subprocess import Popen
from django.contrib.staticfiles.management.commands.runserver import Command as RunserverCommand
from django.conf import settings


class Command(RunserverCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.processes = []

    def run(self, *args, **kwargs):
        if not os.environ.get('RUN_MAIN'):
            try:
                processes_to_run = settings.RUNPROCESS_PROCESSES
            except AttributeError:
                processes_to_run = []

            self.run_processes(processes_to_run)

        super(Command, self).run(*args, **kwargs)

        if not os.environ.get('RUN_MAIN'):
            self.kill_processes()

    def run_processes(self, processes):
        for process in processes:
            p = Popen(process)
            self.processes.append(p)

    def kill_processes(self):
        for process in self.processes:
            process.kill()
