#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p) {
	// Check if the object is a Python list
	if (!PyList_Check(p)) {
		printf("Error: p is not a Python list\n");
		return;
	}

	// Get the length of the list
	Py_ssize_t len = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	// Iterate over the elements of the list
	for (Py_ssize_t i = 0; i < len; i++) {
		PyObject *elem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);
	}
}

void print_python_bytes(PyObject *p) {
	// Check if the object is a Python bytes object
	if (!PyBytes_Check(p)) {
		printf("Error: p is not a Python bytes object\n");
		return;
	}

	// Get the number of bytes in the bytes object
	Py_ssize_t len = PyBytes_Size(p);

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python bytes object = %ld\n", len);
	printf("[*] Trying string: %s\n", PyBytes_AsString(p));

	// Print the first 10 bytes
	printf("[*] First %d bytes: ", len < 10 ? len : 10);
	for (Py_ssize_t i = 0; i < len && i < 10; i++) {
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}


int main(int argc, char *argv[]) {
	// Initialize the Python interpreter
	Py_Initialize();

	// Import the sys module
	PyObject *sys = PyImport_ImportModule("sys");

	// Get the version of Python
	PyObject *version = PyObject_GetAttrString(sys, "version");
	printf("Python version: %s\n", PyUnicode_AsUTF8(version));

	PyObject *list = PyList_New(3);
	PyList_SetItem(list, 0, PyLong_FromLong(1));
	PyList_SetItem(list, 1, PyUnicode_FromString("Hello"));
	PyList_SetItem(list, 2, PyFloat_FromDouble(3.14));
