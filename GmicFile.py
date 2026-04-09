import re


class FiltreGmic:
    def __init__(self, filename):
        self.filename = filename
        self.filters = self.load()

    def load(self):
        filters = {}
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read()
            pattern = r"(\w+)\s*:\s*\n(.*?)(?=\n\w+\s*:|$)"
            matches = re.findall(pattern, content, re.DOTALL)
            for name, body in matches:
                filters[name.strip()] = body.strip()
        except FileNotFoundError:
            pass
        return filters

    def add(self, name, commands):
        lines = [f"{line.strip()}" for line in commands.strip().split("\n")]
        self.filters[name] = "\n".join(lines)
        self.save()

    def remove(self, name):
        try:
            del self.filters[name]
        except Exception as err:
            return False
        self.save()
        return True

    @property
    def liste(self):
        return list(self.filters.keys())

    def get(self, name):
        try:
            return True, self.filters[name]
        except Exception as err:
            return False, ""

    def isin(self, name):
        if name in self.filters:
            return True
        else:
            return False

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for name, body in self.filters.items():
                f.write(f"{name} :\n{body}\n\n")


if __name__ == "__main__":
    filtres = FiltreGmic("filtres_essaie.gmic")
    filtre = """
    fx_voronoi 120,1,0.5
    fx_lightglow 15,0.2
    """
    filtres.add("filtre8943", filtre)

    filtres.remove("filtre4")
    filtres.isin("filtre4")
    print(filtres.liste)
