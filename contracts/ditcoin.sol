// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Ditcoin is ERC20 {

    constructor(uint initialSupply) ERC20("DitCoin, DTC") {
        _mint(msg.sender, initialSupply);
    }

    function offer_dit() public payable {

    }

    function spin() {
    }

    function best_dit() {}
}