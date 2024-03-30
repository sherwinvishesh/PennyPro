import React from 'react';

interface AnalysisProps {
  imageUrls: string[]; // Assuming image URLs are passed as an array of strings
}

const Analysis: React.FC<AnalysisProps> = ({ imageUrls }) => {
  return (
    <div>
      <h1>Analysis</h1> {/* Main Heading */}
      <h2>Charts</h2> {/* Sub-heading */}
      {imageUrls.length > 0 ? (
        imageUrls.map((url, index) => (
          <div key={index}>
            <img src={url} alt={`Analysis Result ${index + 1}`} style={{ maxWidth: '100%', marginBottom: '20px' }} />
          </div>
        ))
      ) : (
        <p>No analysis results to display.</p>
      )}
    </div>
  );
};

export default Analysis;
