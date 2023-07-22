# noqa
import csv


def midle_w(file_path):
    summ_height = 0
    summ_weight = 0
    with open(file_path, newline="") as file:
        reader = csv.DictReader(
            file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL, escapechar="\\"
        )

        for row in reader:
            index = row["Index"]
            # comment = row["Comment"]
            height = float(row["Height(Inches)"])
            # extra = row["Extra"]
            weight = float(row["Weight(Pounds)"])

            summ_height += height
            summ_weight += weight

        md_he = summ_height / float(index)
        md_we = summ_weight / float(index)
        return md_he, md_we
