## Easy Setup

### Install Anaconda

Set your project interpreter to Anaconda's (base) interpreter:
- Windows: `C:\Users\(your_user_name)\anaconda3`
- Ensure Python Version 3.11 for CUDA compatibility.

### Create and Activate Environment

```bash
conda create -n Yolov8_TCL python=3.11
conda activate Yolov8_TCL

### Install Requirements

For Windows & Mac:
```bash
pip install -r requirements.txt

**Note:** If you plan on using a GPU, follow the instructions at [Pytorch's website](https://pytorch.org/get-started/locally/) to install the correct version/build for your machine.

Finally, set your new conda environment (Yolov8_TLC) as your project's python interpreter.

**Enjoy!**