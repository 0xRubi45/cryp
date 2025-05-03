const { ethers } = require("ethers");

async function checkBalance(address) {
  const provider = ethers.getDefaultProvider("mainnet");
  const balance = await provider.getBalance(address);
  console.log(`Balance of ${address}: ${ethers.utils.formatEther(balance)} ETH`);
}

const address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"; // Example
checkBalance(address);
