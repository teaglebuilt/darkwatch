from stem.control import Controller

with Controller.from_port(port = 9051) as controller:
    controller.authenticate()

    bytes_r = controller.get_info("traffic/read")
    bytes_w = controller.get_info("traffic/written")

    print(f"My tor relay has read {bytes_r} and written {bytes_w}")
