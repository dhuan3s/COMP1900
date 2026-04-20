def count_pages(pages_string):
    # split input by commas
    parts = pages_string.split(",")
    total_pages = 0

    # loop through each part
    for part in parts:
        part = part.strip()

        # check if it's a range
        if "-" in part:
            range_parts = part.split("-")
            start_page = int(range_parts[0])
            end_page = int(range_parts[1])

            # handle reversed ranges
            if start_page > end_page:
                temp = start_page
                start_page = end_page
                end_page = temp

            # count pages in range
            total_pages += (end_page - start_page + 1)
        else:
            # single page
            total_pages += 1

    return total_pages

print(count_pages("5-7, 2"))
print(count_pages("12-18, 20-20"))
print(count_pages("18-12, 20-20, 5-6"))