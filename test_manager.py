from box_manager import BoxManager

def my_task():
    print("Doing safe orchestration...")

manager = BoxManager()
manager.load_config_and_orchestrate("orchestration.yaml", my_task)
