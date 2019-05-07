using UnityEngine;
using System;
using System.Runtime.InteropServices;

public class ReadSharedMemory : MonoBehaviour {
    public uint SHARED_MEMORY_SIZE = 1024;
    public string TAG_NAME = "Local\\Test";
    SharedMem map;

    void Start () {
        Debug.Log("[ReadSharedMemory] initializing objects...");
        // only for .NET 4.0 and above
        //MemoryMappedFile mmf = MemoryMappedFile.CreateNew(TAG_NAME, SHARED_MEMORY_SIZE);

        // for all versions of .NET
        map = new SharedMem(TAG_NAME, true, SHARED_MEMORY_SIZE);
    }
	
	void Update () {
        IntPtr root = map.Root;

        if (root == null) {
            Debug.Log("Cannot locate shared memory. Check if the Python side is turned on.");
        }
        else
        {
            string content = Marshal.PtrToStringAnsi(root);
            Debug.Log("content(of shared mem): " + content);
        }
    }
}