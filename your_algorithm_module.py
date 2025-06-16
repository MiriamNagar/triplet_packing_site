# your_algorithm_module.py

def run_algorithm(items, binsize):
    # Dummy implementation — replace with your actual logic
    bins = []
    current_bin = []
    current_sum = 0

    for item in items:
        if current_sum + item <= binsize:
            current_bin.append(item)
            current_sum += item
        else:
            bins.append(current_bin)
            current_bin = [item]
            current_sum = item
    if current_bin:
        bins.append(current_bin)

    output = "\n".join(f"Bin {i + 1}: {b}" for i, b in enumerate(bins))
    logs = f"Total bins used: {len(bins)}\nItems: {items}\nBin size: {binsize}"
    return output, logs
