#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	int size, allocation, i;
	PyObject *p_obj;

	size = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		p_obj = PyList_GET_ITEM(p, i);
		printf("%s\n", Py_TYPE(p_obj)->tp_name);
	}
}
