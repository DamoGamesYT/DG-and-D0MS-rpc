from pypresence import Presence
import time

###################
## -Discord RPC- ##
###################

buttonList = [
    {
        "label": "Damos Discord",
        "url": "https://discord.io/Gamesclub"
    },
    {
        "label": "damos site",
        "url": "https://damogames.ga"
    }
]

rpc = Presence("898598692330823680")
rpc.connect()
rpc.update(
    details="Damos Rpc",
    large_text="Damos rpc",
    large_image="laspect",
    small_text="by Dom",
    small_image="rpc",
    buttons=buttonList,
    start=time.time()
)

while 1:
    time.sleep(1)