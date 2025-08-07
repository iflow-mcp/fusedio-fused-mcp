
# Fused Multi-Step Job

## Get started
```python
# Import UDFs
from udf_tree_height_stats_from_lat_lon import tree_height_stats_from_lat_lon

# Instantiate individual jobs
job_tree_height_stats_from_lat_lon = tree_height_stats_from_lat_lon(lon, lat=49.2426)

# Instantiate multi-step job
job = fused.experimental.job([job_tree_height_stats_from_lat_lon])

# Run locally
job.run_local(file_id=0, chunk_id=0)

# Run remotely
job.run_remote(output_table='output_table_name')
```
