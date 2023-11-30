class DebugTool:
  def __init__(self) -> None:
    return
    
  def print_options(self, options) -> None:
    print("---------------- chrome_options ----------------")
    for arg in options._arguments:
        print(arg)
    return