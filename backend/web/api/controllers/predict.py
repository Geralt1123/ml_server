import os
from dataclasses import dataclass
from ultralytics import YOLO
from interfaces import AsyncService
import numpy as np
from PIL import Image


@dataclass(kw_only=True, slots=True, frozen=True)
class PredictController(AsyncService):

    async def __call__(
            self,
            file: bytes
    ):
        arr = file.root
        arr = np.array(arr)

        if isinstance(arr, np.ndarray):
            if arr.dtype == np.float32 or arr.dtype == np.float64:
                arr = arr.astype(np.uint8)

        im = Image.fromarray(arr, 'L')
        im.save("detect.jpeg")
        # Load a pre-trained YOLOv10n model
        model = YOLO("best_const.pt")

        # Perform object detection on an image
        results = model("detect.jpeg")

        os.remove("detect.jpeg")
        # Display the results

        return results[0].orig_img.tolist()


@dataclass(kw_only=True, slots=True, frozen=True)
class PredictControllerTwo(AsyncService):

    async def __call__(
            self,
            file: bytes
    ):
        arr = file.root
        arr = np.array(arr)

        if isinstance(arr, np.ndarray):
            if arr.dtype == np.float32 or arr.dtype == np.float64:
                arr = arr.astype(np.uint8)

        im = Image.fromarray(arr, 'L')
        im.save("detect_2.jpeg")
        # Load a pre-trained YOLOv10n model
        model = YOLO("best_def.pt")

        # Perform object detection on an image
        results = model("detect_2.jpeg")

        os.remove("detect_2.jpeg")
        # Display the results

        return results[0].orig_img.tolist()
