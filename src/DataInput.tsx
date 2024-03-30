// DataInput.tsx
import React, { useState, ChangeEvent, FormEvent } from 'react';

interface FormData {
  expenseOn: string;
  expenseType: string;
  amount: string;
  date: string;
}

export const DataInput: React.FC<{ onStartAnalysis: () => void }> = ({ onStartAnalysis }) => {
  const [formData, setFormData] = useState<FormData[]>([{ expenseOn: '', expenseType: '', amount: '', date: '' }]);
  const [file, setFile] = useState<File | null>(null);

  const handleInputChange = (index: number, e: ChangeEvent<HTMLInputElement>) => {
    const newFormData = [...formData];
    newFormData[index][e.target.name as keyof FormData] = e.target.value;
    setFormData(newFormData);
  };

  const handleAddRow = () => {
    setFormData([...formData, { expenseOn: '', expenseType: '', amount: '', date: '' }]);
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    console.log('Form Data:', formData);
    console.log('CSV File:', file);
    onStartAnalysis(); // Invoke the callback to signal readiness to start analysis
  };

  return (
    <div>
      <h2>Enter Expense Details or Upload a CSV File</h2>
      <form onSubmit={handleSubmit}>
        {formData.map((data, index) => (
          <div key={index}>
            <input type="text" name="expenseOn" placeholder="Expense On (e.g., Domino's)" value={data.expenseOn} onChange={(e) => handleInputChange(index, e)} />
            <input type="text" name="expenseType" placeholder="Expense Type (e.g., Food)" value={data.expenseType} onChange={(e) => handleInputChange(index, e)} />
            <input type="text" name="amount" placeholder="Amount" value={data.amount} onChange={(e) => handleInputChange(index, e)} />
            <input type="date" name="date" value={data.date} onChange={(e) => handleInputChange(index, e)} />
            {index === formData.length - 1 && <button type="button" onClick={handleAddRow}>Add More Data</button>}
          </div>
        ))}
        <div>
          <label htmlFor="csvUpload">Or upload a CSV file:</label>
          <input type="file" id="csvUpload" accept=".csv" onChange={handleFileChange} />
        </div>
        <button type="submit">Start Analysis</button>
      </form>
    </div>
  );
};
