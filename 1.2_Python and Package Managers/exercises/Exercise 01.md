# Environment Exercise

1. Create a new folder where you will host an environment for this exercise. You can call it `exercise-env`.
2. Check your installed Python version and take note of it.
3. Use `virtualenv` to create a new environment called `env` inside this folder using your installed Python version.
4. Activate the environment.
5. Install packages `matplotlib` and `numpy`.
6. Create a new Python script called `graph.py` and paste the following code.

```
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
```

7. Save the file and run it.
   > Note: If when running it returns an error `ImportError: DLL load failed while importing _cext: The specified module could not be found.`, it means you do not have C++ Redistributable installed on your machine. You can download and install it from here `https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170`.
8. Now create a `requirements.txt` file by exporting all required libraries from this environment.
9. Now, create a new folder outside this folder named `exercise-env-2`.
10. Copy `graph.py` and `requirements` from `exercise-env` to this folder.
11. Create a new environment `env` inside the new folder.
12. Activate the environment, and install the requirements from the `requirements.txt` file.
13. Run the script `graph.py` and check that it works.

<details>
<summary>Answers</summary>

```
mkdir exercise-env
python --version
python -m virtualenv --python=3.12 env
.\env\Scripts\activate
pip install matplotlib numpy
python -m pip freeze > requirements.txt
cd..
mkdir exercise-env-2
cp .\exercise-env\graph.py .\exercise-env-2
cp .\exercise-env\requirements.txt .\exercise-env-2
cd exercise-env-2
python -m virtualenv --python=3.12 env
pip install -r requirements.txt
```

</details>
