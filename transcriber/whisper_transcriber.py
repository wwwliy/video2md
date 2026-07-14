from faster_whisper import WhisperModel

import os
import json


class WhisperTranscriber:

    def __init__(
        self,
        model_name="small",
        device="cpu",
        compute_type="int8"
    ):

        print(f"\nLoading Faster-Whisper ({model_name})...")

        self.model = WhisperModel(
            model_name,
            device=device,
            compute_type=compute_type
        )

        print("Model loaded.\n")

    def transcribe(self, video_path):

        print("Start transcribing...\n")

        segments, info = self.model.transcribe(
            video_path,
            beam_size=1,
            vad_filter=False
        )

        all_text = ""

        segment_list = []

        for seg in segments:

            print(
                f"[{self.sec2time(seg.start)} --> {self.sec2time(seg.end)}] {seg.text}"
            )

            all_text += seg.text.strip() + "\n"

            segment_list.append({
                "start": seg.start,
                "end": seg.end,
                "text": seg.text.strip()
            })

        result = {
            "language": info.language,
            "duration": getattr(info, "duration", None),
            "text": all_text.strip(),
            "segments": segment_list
        }

        self.save_result(video_path, result)

        return result

    def save_result(self, video_path, result):

        output_dir = "output"

        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.splitext(
            os.path.basename(video_path)
        )[0]

        txt_file = os.path.join(
            output_dir,
            filename + ".txt"
        )

        srt_file = os.path.join(
            output_dir,
            filename + ".srt"
        )

        json_file = os.path.join(
            output_dir,
            filename + ".json"
        )

        # 保存 txt

        with open(
            txt_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(result["text"])

        # 保存 srt

        with open(
            srt_file,
            "w",
            encoding="utf-8"
        ) as f:

            for index, seg in enumerate(
                result["segments"],
                start=1
            ):

                f.write(f"{index}\n")

                f.write(
                    f"{self.sec2time(seg['start'])} --> "
                    f"{self.sec2time(seg['end'])}\n"
                )

                f.write(seg["text"] + "\n\n")

        # 保存 json

        with open(
            json_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                result,
                f,
                ensure_ascii=False,
                indent=2
            )

        print("\n===========================")
        print("Output files:")
        print(txt_file)
        print(srt_file)
        print(json_file)
        print("===========================\n")

    @staticmethod
    def sec2time(seconds):

        h = int(seconds // 3600)

        m = int((seconds % 3600) // 60)

        s = int(seconds % 60)

        ms = int((seconds - int(seconds)) * 1000)

        return f"{h:02}:{m:02}:{s:02},{ms:03}"