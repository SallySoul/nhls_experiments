import os

def make_work_dir(prefix, parent_dir):
    # To an array of all folders in the directory
    arr = os.listdir(parent_dir)
    
    folder_nums = [0]
    
    for folder_name in arr:
      
      # Spilts the string into ["NewDir","1"]
      num_component = folder_name.split("_")[-1]
      folder_nums.append( int(num_component) )
    
    new_folder_num = max(folder_nums) + 1 

    new_folder_path = f"{parent_dir}/{prefix}_{new_folder_num:04d}"

    print(f"*** MAKE WORK DIR: {new_folder_path}")
    os.mkdir(new_folder_path)

    return new_folder_path
