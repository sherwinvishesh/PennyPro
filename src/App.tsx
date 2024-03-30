// App.tsx
import React, { useState } from 'react';
import { ConnectButton, useCurrentAccount } from "@mysten/dapp-kit";
import { Box, Container, Flex, Heading } from "@radix-ui/themes";
import { DataInput } from './DataInput';
import Analysis from './Analysis';

const predefinedImageUrls = [
  'static/images/monthly_expense_breakdown.png',
  'static/images/predictive_spending_entertainment.png',
  'static/images/predictive_spending_food.png',
  'static/images/predictive_spending_insurance.png',
  'static/images/predictive_spending_miscellaneous.png',
  'static/images/predictive_spending_transportation.png',
  'static/images/predictive_spending_utilities.png',
  'static/images/savings_opportunity.png',
  'static/images/spending_efficiency_radar_chart.png',
];



function App() {
  const currentAccount = useCurrentAccount();
  const [view, setView] = useState<'welcome' | 'dataInput' | 'analysis'>('welcome');
  const [imageUrls, setImageUrls] = useState<string[]>([]); // Add this line

  const handleStartAnalysis = () => {
    setImageUrls(predefinedImageUrls); // Use predefined URLs
    setView('analysis'); // Switch to the analysis view
  };

  return (
    <>
      <Flex position="sticky" px="4" py="2" justify="between" style={{ borderBottom: "1px solid var(--gray-a2)" }}>
        <Box><Heading>PennyPro</Heading></Box>
        <Box><ConnectButton /></Box>
      </Flex>
      <Container mt="5" pt="2" px="4" style={{ background: "var(--gray-a2)", minHeight: 500 }}>
        {view === 'welcome' && currentAccount ? (
          <>
            <Heading>Welcome, {currentAccount.address}</Heading>
            <button onClick={() => setView('dataInput')}>Enter Financial Details</button>
          </>
        ) : !currentAccount ? (
          <Heading>Please connect your wallet</Heading>
        ) : null}
        {view === 'dataInput' && <DataInput onStartAnalysis={handleStartAnalysis} />}
        {view === 'analysis' && <Analysis imageUrls={imageUrls} />}
      </Container>
    </>
  );
}

export default App;
