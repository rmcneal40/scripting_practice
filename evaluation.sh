# #!/bin/bash
# echo “Evaluating this computer…”
# echo “Computer Name: “$(lshw | grep “” -ml) # Looking for a better way to do this
# echo “CPU: “$(lshw | grep “*-cpu” -A 5)
# echo “RAM: “$(lshw | grep “*-memory” -A 3)
# echo “Display Adapter: “$(lshw | grep “*-display” A 10)
# echo “Network Adapter: “$(lshw | grep “*-network” -A 15)
# echo “Evalution complete.”

 function Evaluate() {
    echo "Evaluating this computer is becoming more challenging"
}
Evaluate

function Lenovo() {
    echo "Computer Name: Lenovo "$(lshw | grep "" -ml) 
}
Lenovo
