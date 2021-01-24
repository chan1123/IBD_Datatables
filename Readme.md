# Stock_Datatables

Use Stock datatables to practice data cleaning. 

# Requirements

See requirements.txt

# Usage

Fork/Clone the repository.
```python
import pandas as pd
from functions import read_ibd, convert_datatypes_ibd
from functions import latest_file

df = convert_datatypes_ibd(read_ibd(latest_file()))
```

# RS Rating

Look for RS greater than 80

```python
df[df['RS Rating'] > 80] 
```

