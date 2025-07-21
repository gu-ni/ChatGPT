####################################

python change_coding_into_narrative_other_model.py

for ((i=1; i<=100000; i++)); do
    echo "$i"
    python /home/work/users/PIL_ghj/LLM/code/generate_qa_datasets_copy.py
done
