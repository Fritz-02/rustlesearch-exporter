Rustlesearch Exporter
=======
Some tools for exporting Rustlesearch.dev logs to a text file, and merging exported files together.

Usage
-----

.. code:: sh

    # For exporting logs
    python3 log_exporter.py -U cake -T pepoturkey -S 2023-01-01 -E 2023-01-31 -o cake_gobbles.txt
    python3 log_exporter.py -U JaydrVernanda -T tonyw -S 2023-01-01 -E 2023-01-31 -o jaydr_tonys.txt

    # For merging log files
    python3 logs_merger.py cake_gobbles.txt jaydr_tonys.txt -o gobbling_tonys.txt

    # Get all options available
    python3 log_exporter.py -h
    python3 logs_merger.py -h

