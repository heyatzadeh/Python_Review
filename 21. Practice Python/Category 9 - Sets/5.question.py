# Remove items 10, 20, 30 from the following set at once

set = {10, 20, 30, 40, 50}

set.difference_update({10, 20, 30})
print(set)
