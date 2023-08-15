import os

# Transforming .json to .tsv
plotting_data_paths = [
    # "real/retweets/post_analysis/plotting_data",
    # "real/retweets_2d/post_analysis/plotting_data",
    
    # "synth/crisp/100x100x100/post_analysis/plotting_data",
    # "synth/crisp/1000x1000/post_analysis/plotting_data",

    "synth/fuzzy/100x100x100/post_analysis/plotting_data",
    # "synth/fuzzy/1000x1000/post_analysis/plotting_data",
    ]

for plotting_data_path in plotting_data_paths:
    for folder in os.listdir(plotting_data_path):
        path = os.path.join(plotting_data_path, folder)

        for json_file in os.listdir(path):
            json_file_path = os.path.join(path, json_file)
            tsv_file_path = json_file_path.replace(".json", ".tsv")

            command = f"""jq -r '[.x, .y] | transpose | map(@tsv) | join("\n")' {json_file_path} > {tsv_file_path}"""
            os.system(command)