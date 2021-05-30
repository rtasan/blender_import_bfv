import bpy
import os
import glob
import time


data_dir = r"C:\Users\Reiko\Documents\gitprojects\blender_import_bfv\example_models\model1"

def import_bfv(folder_path):
    bpy.ops.object.select_all(action='DESELECT')
    os.chdir(folder_path)
    paths = glob.glob("*.fbx")
    print(paths)
    for path in paths:
        bpy.ops.import_scene.fbx(filepath = path)
        
        
    # to change mode safely, set active first
    bpy.context.view_layer.objects.active = bpy.data.objects['Reference']
    bpy.ops.object.mode_set(mode = "OBJECT")
    
    
    
    
    for obj in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        if 'lod0' in obj.name:
            
            # Change modifier settings
            for m in obj.modifiers:
                if m.type == 'ARMATURE':
                    m.object = bpy.data.objects["Reference"]
            obj.parent =  bpy.data.objects['Reference']
            
        elif 'Reference' in obj.name:
            
            obj.select_set(True)
            
            # Apply Armature rotation
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)       
            
        else:
            bpy.data.objects.remove(obj)


    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj.name != 'Reference':
            bpy.data.objects.remove(obj)
            
        
        
        
start = int(time.time() * 1000.0)

# do it!
import_bfv(data_dir)

print("All done in " + str(int((time.time() * 1000.0) - start)) + "ms")

