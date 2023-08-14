import os
import json
from statistics import mean

# # Transforming .json to .tsv
# plotting_data_paths = [
#     "real/retweets/post_analysis/plotting_data",
#     "real/retweets_2d/post_analysis/plotting_data",
    
#     "synth/crisp/100x100x100/post_analysis/plotting_data",
#     "synth/crisp/1000x1000/post_analysis/plotting_data",

#     "synth/fuzzy/100x100x100/post_analysis/plotting_data",
#     "synth/fuzzy/1000x1000/post_analysis/plotting_data",
#     ]

# for plotting_data_path in plotting_data_paths:
#     for folder in os.listdir(plotting_data_path):
#         path = os.path.join(plotting_data_path, folder)

#         for json_file in os.listdir(path):
#             json_file_path = os.path.join(path, json_file)
#             tsv_file_path = json_file_path.replace(".json", ".tsv")

#             command = f"""jq -r '[.x, .y] | transpose | map(@tsv) | join("\n")' {json_file_path} > {tsv_file_path}"""
#             os.system(command)


iteration_paths = [
    "synth/crisp/100x100x100/iterations",
    # "synth/crisp/1000x1000/iterations",

    # "synth/fuzzy/100x100x100/iterations",
    # "synth/fuzzy/1000x1000/iterations",
]

for iteration_path in iteration_paths:
    for co in [1,2,4,8,16]:

        tensor_path = "tensors"
        extension = None
        if "crisp" in iteration_path:
            tensor_path = f"{tensor_path}/crisp"
            extension = "crisp_tensor"
        if "fuzzy" in iteration_path:
            tensor_path = f"{tensor_path}/numnoise"
            extension = "fuzzy_tensor"

        tensor_path = f"{tensor_path}/dataset-co{co}.{extension}"

        empty_model_rss_s = []

        for iteration in range(1, 31):
            path = f"{iteration}/{tensor_path}"
            path = os.path.join(iteration_path, path)

            rss = os.system(f"null-model-rss {path}")
            empty_model_rss_s.append(rss)

        tsv_path = iteration_path.replace("iterations", "post_analysis")
        tsv_path = f"{tsv_path}/plotting_data/rssevolution"

        print(empty_model_rss_s)

        # for tsv_file in os.listdir(tsv_path):
        #     if f"co{co}" in tsv_file:
        #         tsv_file_path = os.path.join(tsv_path, tsv_file)

        #         with open(tsv_file_path, "w") as f:
        #             lines = f.readlines()

        #             mean_rss = mean(empty_model_rss_s)

        #             print(f"Writing {mean_rss: .4f} to {tsv_file_path}")
        #             f.write(f"0  {mean_rss}\n")

        #             for line in lines:
        #                 f.write(line)