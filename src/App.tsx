// App.tsx
import React, { useState } from 'react';
import { ConnectButton, useCurrentAccount } from "@mysten/dapp-kit";
import { Box, Container, Flex, Heading } from "@radix-ui/themes";
import { DataInput } from './DataInput';
import { Analysis } from './Analysis'; // Assume you've created this component

function App() {
  const currentAccount = useCurrentAccount();
  const [view, setView] = useState<'welcome' | 'dataInput' | 'analysis'>('welcome');

  const handleStartAnalysis = () => {
    setView('analysis'); // This function will be called by DataInput to switch to the analysis view
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
        {view === 'analysis' && <Analysis />}
      </Container>
    </>
  );
}

export default App;
