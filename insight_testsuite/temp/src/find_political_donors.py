import sys
from HelperModule import InputProcessor
import time

def find_political_donors():
    # debugging timing
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Please enter input filename")
        sys.exit(0)

    # set default in case no output path is specified
    inputfilename = sys.argv[1]
    f_out1 = "medianvals_by_date.txt"
    f_out2 = "medianvals_by_zip.txt"

    if len(sys.argv) == 4:
        print("output file specified")
        f_out1 = sys.argv[3]
        f_out2 = sys.argv[2]

    f_in = open(inputfilename, "r")

    try:
        m_date = open(f_out1, "w")
        m_zip = open(f_out2, "w")
    except:
        print("Failed to open " + f_out1 + " or " + f_out2)

    input_handler = InputProcessor()
    # memory efficient way of reading a file
    for line in f_in:
        input_handler.process_input(line)
        # get line_zip
        line_zip = input_handler.get_zip_result()

        if line_zip is not None:
            m_zip.write(line_zip + "\n")

    # get date_map
    date_map = input_handler.get_date_result()
    date_rez_set = []
    if len(date_map) > 0:
        for date_id, median_queue in date_map.items():
            date_rez = []
            date_rez.append(date_id[0:9])
            date_rez.append(date_id[9:])
            # median, count, total
            date_rez.append(median_queue.get_median())
            date_rez.append(median_queue.get_queue_len())
            date_rez.append(median_queue.get_total())
            date_rez_set.append("|".join(date_rez)+"\n")

    # write all to m_date
    m_date.writelines(date_rez_set)

    # close files
    f_in.close()
    m_date.close()
    m_zip.close()
    print("program executed: %s" %(time.time() - start_time))

if __name__ == "__main__":
    find_political_donors()
