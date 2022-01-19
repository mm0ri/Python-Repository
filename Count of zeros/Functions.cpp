#include <iostream>
#include "Functions.h"
#include "Param.h"

using namespace std;

void NumberInput() // Also i tryed to make rule that u cant enter a word. Only numbers, but nothing work :(
{
	cout << "=============================" << endl;
	cout << "Enter your number from 0 to 21:" << endl;
	cin >> Number;
	cout << endl;
}

void FactorialFunction()
{

	for (int i = 1; i <= Number; ++i)
	{
		F *= i;
	}
	cout << "Number Factorial:" << endl;
	cout << F << endl;
}

void FactorialCounter()
{
	while (F % 10 == 0)
	{
		Counter += 1;
		F = F / 10;
	}
	cout << "Count of zeros in the end:" << endl;
	cout << Counter << endl;
}

void MainFunction()
{
	if (Number >= 0 && Number <= 20) // We can't use number more than 20. Why? Because we don't have data type more than long long int (18,446,744,073,709,551,615) That's sad :(
	{
		FactorialFunction();
		FactorialCounter();
	}
	else
	{
		cout << "You make mistake! Check rules again :)";
	}
}
