"""#16 — asyncio.Lock: mutual exclusion for shared async state."""
import asyncio


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        self._lock = asyncio.Lock()

    async def transfer_out(self, amount: float, label: str):
        async with self._lock:
            print(f"  [{label}] checking balance: {self.balance}")
            await asyncio.sleep(0.5)
            if self.balance >= amount:
                self.balance -= amount
                print(f"  [{label}] withdrew {amount}, new balance: {self.balance}")
            else:
                print(f"  [{label}] insufficient funds!")


async def main():
    account = BankAccount(100)
    await asyncio.gather(
        account.transfer_out(80, "ATM-1"),
        account.transfer_out(80, "ATM-2"),
    )
    print(f"Final balance: {account.balance}")


if __name__ == "__main__":
    asyncio.run(main())
