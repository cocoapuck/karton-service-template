from karton.core import Karton, Task, Resource, Config
from karton.utils import Utils
from .__version__ import __version__
import subprocess


class %UCASE_CLASS%(Karton):
    
    
    name = "%CLASS%"
    identity = f"karton.{name}"
    version = __version__
    filters = [{"type": "sample", "stage": "recognized"}]
    producer_filter = {"type": "sample", "stage": "analyzed"}
    tags = [f"{name}:"]
    create_new_file = True

    
    def process(self, task: Task) -> None:
        try:
            sample_resource = task.get_resource("sample")
            self.log.info(f"Starting {self.name} analysis on: {sample_resource.name}")
            attributes = Utils().get_file_attributes(sample_resource.sha256)
            
            with sample_resource.download_temporary_file() as sample_file:
                result = subprocess.check_output(["strings", sample_file.name])

            task = Task(
                {"type": "sample", "stage": "analyzed"},
                payload={"parent": sample_resource, "tags": self.tags, "attributes": attributes, "sample": Resource(f"{sample_resource.name}_{self.name}", result)},
            )
            self.send_task(task)

            task = Task(
                {"type": "sample", "stage": "analyzed"},
                payload={"tags": self.tags, "sample": sample_resource},
            )
            self.send_task(task)

        except:
            self.log.error(f"Error in string analysis on: {sample_resource.name}")