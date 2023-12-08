class PrePro:
    @staticmethod
    def filter(code):
        lines = code.split("\n")
        code_filtered = ""
        for line in lines:
            code_filtered += line.split("//")[0] + "\n"
        return code_filtered
