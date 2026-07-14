import re


class SectionSplitter:

    def split(self, text: str):

        text = text.replace("\r", "")

        paragraphs = []

        current = []

        sentence_count = 0

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            current.append(line)

            sentence_count += len(
                re.findall(r"[。！？!?；;]", line)
            )

            if sentence_count >= 5:

                paragraphs.append("\n".join(current))

                current = []

                sentence_count = 0

        if current:
            paragraphs.append("\n".join(current))

        result = []

        for i, p in enumerate(paragraphs, start=1):

            result.append({

                "title": f"主题{i}",

                "content": p

            })

        return result