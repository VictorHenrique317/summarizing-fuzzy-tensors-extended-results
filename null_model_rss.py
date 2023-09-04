import os
from statistics import mean
import subprocess
import re

# Adding null model rss to plotting_data
iteration_paths = [
    # "synth/crisp/100x100x100/iterations",
    # "synth/crisp/1000x1000/iterations",

    "synth/fuzzy/100x100x100/iterations",
    # "synth/fuzzy/1000x1000/iterations",
]

for iteration_path in iteration_paths:
    for co in [1,2,4,8,16]:

        extension = "fuzzy_tensor"
        tensor_path = "tensors/numnoise"

        tensor_path = f"{tensor_path}/dataset-co{co}.{extension}"

        empty_model_rss_s = []
        nb_iterations = 5

        for iteration in range(1, nb_iterations + 1):
            print(f"{iteration/nb_iterations*100: .2f}%", end="\r")
            
            path = f"{iteration}/{tensor_path}"
            path = os.path.join(iteration_path, path)

            rss = subprocess.check_output(f"null-model-rss {path}", shell=True, text=True).strip()
            empty_model_rss_s.append(float(rss))

        tsv_path = iteration_path.replace("iterations", "post_analysis")
        tsv_path = f"{tsv_path}/rssevolution"

        print(f"co{co} - mean {mean(empty_model_rss_s): .4f}")
        answer = input(f"Insert {mean(empty_model_rss_s): .4f} in all co{co}? (y/n)")
        # answer = "y"

        if answer == "y":
            for tsv_file in os.listdir(tsv_path):
                pattern = "(\d+)"

                match = re.search(pattern, tsv_file)
                match = int(match.group(0))

                if match == co:
                    tsv_file_path = os.path.join(tsv_path, tsv_file)

                    lines = None
                    with open(tsv_file_path, "r") as f:
                        lines = f.readlines()

                    with open(tsv_file_path, "w") as f:
                        mean_rss = mean(empty_model_rss_s)

                        print(f"Writing {mean_rss: .4f} to {tsv_file_path}")
                        f.write(f"0\t{mean_rss}\n")

                        for line in lines:
                            f.write(line)