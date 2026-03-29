import json

metadata_path = "/home/diogo/dev/library-docs/gemini-cli/metadata.json"
with open(metadata_path, "r") as f:
    metadata = json.load(f)

unique_keys = set()
for doc in metadata["documents"]:
    orig_path = doc.get("original_file_path")
    if not orig_path:
        curr_path = doc["file_path"]
        if len(curr_path) > 4 and curr_path[3] == "-":
            orig_path = curr_path[4:]
        else:
            orig_path = curr_path
    unique_keys.add(orig_path)

print(sorted(list(unique_keys)))
