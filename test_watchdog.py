#!/usr/local/bin/python
import sys
import time
import watchdog
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.rar"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # ithe file will be processed there
        if str(event.event_type) == 'created':
            print("Event Type: {1}\nSource path: {0}").format(event.src_path, event.event_type)  # print now only for degug
        elif str(event.event_type) == 'moved' :
            print("Event Type: {1}\nSource path: {0}\nDest path: {2}").format(event.src_path, event.event_type, event.dest_path)  # print now only for degug
            

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)
        
    #def on_any_event(self, event):
        #self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
