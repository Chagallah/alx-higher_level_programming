#include <Python.h>

void print_python_list_info(PyObject *p)
{
	// Check if p is a list
	if (!PyList_Check(p))
	{
		printf("Error: p is not a Python list\n");
		return;
	}

	// Get the length of the list
	Py_ssize_t len = PyList_Size(p);

	printf("List length: %ld\n", len);

	// Iterate over the list and print the type of each element
	for (Py_ssize_t i = 0; i < len; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("List item %ld: type %s\n", i, item->ob_type->tp_name);
	}
}
