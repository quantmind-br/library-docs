---
title: Retrieval-Augmented Generation (RAG) - DSPy
url: https://dspy.ai/tutorials/rag/
source: sitemap
fetched_at: 2026-01-23T08:04:18.750187698-03:00
rendered_js: false
word_count: 1923
summary: This document explains the concepts of High Memory (HIGHMEM) and Low Memory (LOWMEM) in the Linux kernel, detailing their roles in memory mapping and addressing limitations on 32-bit systems.
tags:
    - linux-kernel
    - memory-management
    - highmem
    - lowmem
    - virtual-memory
    - kernel-space
category: concept
---

```


[2024-11-23T23:16:49.175612]

System message:

Your input fields are:
1. `context` (str)
2. `question` (str)

Your output fields are:
1. `reasoning` (str)
2. `response` (str)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## context ## ]]
{context}

[[ ## question ## ]]
{question}

[[ ## reasoning ## ]]
{reasoning}

[[ ## response ## ]]
{response}

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        Given the fields `context`, `question`, produce the fields `response`.


User message:

[[ ## context ## ]]
[1] «As far as I remember, High Memory is used for application space and Low Memory for the kernel. Advantage is that (user-space) applications cant access kernel-space memory.»
[2] «HIGHMEM is a range of kernels memory space, but it is NOT memory you access but its a place where you put what you want to access. A typical 32bit Linux virtual memory map is like: 0x00000000-0xbfffffff: user process (3GB) 0xc0000000-0xffffffff: kernel space (1GB) (CPU-specific vector and whatsoever are ignored here). Linux splits the 1GB kernel space into 2 pieces, LOWMEM and HIGHMEM. The split varies from installation to installation. If an installation chooses, say, 512MB-512MB for LOW and HIGH mems, the 512MB LOWMEM (0xc0000000-0xdfffffff) is statically mapped at the kernel boot time; usually the first so many bytes of the physical memory is used for this so that virtual and physical addresses in this range have a constant offset of, say, 0xc0000000. On the other hand, the latter 512MB (HIGHMEM) has no static mapping (although you could leave pages semi-permanently mapped there, but you must do so explicitly in your driver code). Instead, pages are temporarily mapped and unmapped here so that virtual and physical addresses in this range have no consistent mapping. Typical uses of HIGHMEM include single-time data buffers.»
[3] «This is relevant to the Linux kernel; Im not sure how any Unix kernel handles this. The High Memory is the segment of memory that user-space programs can address. It cannot touch Low Memory. Low Memory is the segment of memory that the Linux kernel can address directly. If the kernel must access High Memory, it has to map it into its own address space first. There was a patch introduced recently that lets you control where the segment is. The tradeoff is that you can take addressable memory away from user space so that the kernel can have more memory that it does not have to map before using. Additional resources: http://tldp.org/HOWTO/KernelAnalysis-HOWTO-7.html http://linux-mm.org/HighMemory»
[4] «The first reference to turn to is Linux Device Drivers (available both online and in book form), particularly chapter 15 which has a section on the topic. In an ideal world, every system component would be able to map all the memory it ever needs to access. And this is the case for processes on Linux and most operating systems: a 32-bit process can only access a little less than 2^32 bytes of virtual memory (in fact about 3GB on a typical Linux 32-bit architecture). It gets difficult for the kernel, which needs to be able to map the full memory of the process whose system call its executing, plus the whole physical memory, plus any other memory-mapped hardware device. So when a 32-bit kernel needs to map more than 4GB of memory, it must be compiled with high memory support. High memory is memory which is not permanently mapped in the kernels address space. (Low memory is the opposite: it is always mapped, so you can access it in the kernel simply by dereferencing a pointer.) When you access high memory from kernel code, you need to call kmap first, to obtain a pointer from a page data structure (struct page). Calling kmap works whether the page is in high or low memory. There is also kmap_atomic which has added constraints but is more efficient on multiprocessor machines because it uses finer-grained locking. The pointer obtained through kmap is a resource: it uses up address space. Once youve finished with it, you must call kunmap (or kunmap_atomic) to free that resource; then the pointer is no longer valid, and the contents of the page cant be accessed until you call kmap again.»
[5] «/proc/meminfo will tell you how free works, but /proc/kcore can tell you what the kernel uses. From the same page: /proc/kcore This file represents the physical memory of the system and is stored in the ELF core file format. With this pseudo-file, and an unstripped kernel (/usr/src/linux/vmlinux) binary, GDB can be used to examine the current state of any kernel data structures. The total length of the file is the size of physical memory (RAM) plus 4KB. /proc/meminfo This file reports statistics about memory usage on the system. It is used by free(1) to report the amount of free and used memory (both physical and swap) on the system as well as the shared memory and buffers used by the kernel. Each line of the file consists of a parameter name, followed by a colon, the value of the parameter, and an option unit of measurement (e.g., kB). The list below describes the parameter names and the format specifier required to read the field value. Except as noted below, all of the fields have been present since at least Linux 2.6.0. Some fields are displayed only if the kernel was configured with various options; those dependencies are noted in the list. MemTotal %lu Total usable RAM (i.e., physical RAM minus a few reserved bits and the kernel binary code). MemFree %lu The sum of LowFree+HighFree. Buffers %lu Relatively temporary storage for raw disk blocks that shouldnt get tremendously large (20MB or so). Cached %lu In-memory cache for files read from the disk (the page cache). Doesnt include SwapCached. SwapCached %lu Memory that once was swapped out, is swapped back in but still also is in the swap file. (If memory pressure is high, these pages dont need to be swapped out again because they are already in the swap file. This saves I/O.) Active %lu Memory that has been used more recently and usually not reclaimed unless absolutely necessary. Inactive %lu Memory which has been less recently used. It is more eligible to be reclaimed for other purposes. Active(anon) %lu (since Linux 2.6.28) [To be documented.] Inactive(anon) %lu (since Linux 2.6.28) [To be documented.] Active(file) %lu (since Linux 2.6.28) [To be documented.] Inactive(file) %lu (since Linux 2.6.28) [To be documented.] Unevictable %lu (since Linux 2.6.28) (From Linux 2.6.28 to 2.6.30, CONFIG_UNEVICTABLE_LRU was required.) [To be documented.] Mlocked %lu (since Linux 2.6.28) (From Linux 2.6.28 to 2.6.30, CONFIG_UNEVICTABLE_LRU was required.) [To be documented.] HighTotal %lu (Starting with Linux 2.6.19, CONFIG_HIGHMEM is required.) Total amount of highmem. Highmem is all memory above ~860MB of physical memory. Highmem areas are for use by user-space programs, or for the page cache. The kernel must use tricks to access this memory, making it slower to access than lowmem. HighFree %lu (Starting with Linux 2.6.19, CONFIG_HIGHMEM is required.) Amount of free highmem. LowTotal %lu (Starting with Linux 2.6.19, CONFIG_HIGHMEM is required.) Total amount of lowmem. Lowmem is memory which can be used for everything that highmem can be used for, but it is also available for the kernels use for its own data structures. Among many other things, it is where everything from Slab is allocated. Bad things happen when you're out of lowmem. LowFree %lu (Starting with Linux 2.6.19, CONFIG_HIGHMEM is required.) Amount of free lowmem. MmapCopy %lu (since Linux 2.6.29) (CONFIG_MMU is required.) [To be documented.] SwapTotal %lu Total amount of swap space available. SwapFree %lu Amount of swap space that is currently unused. Dirty %lu Memory which is waiting to get written back to the disk. Writeback %lu Memory which is actively being written back to the disk. AnonPages %lu (since Linux 2.6.18) Non-file backed pages mapped into user-space page tables. Mapped %lu Files which have been mapped, such as libraries. Shmem %lu (since Linux 2.6.32) [To be documented.] Slab %lu In-kernel data structures cache. SReclaimable %lu (since Linux 2.6.19) Part of Slab, that might be reclaimed, such as caches. SUnreclaim %lu (since Linux 2.6.19) Part of Slab, that cannot be reclaimed on memory pressure. KernelStack %lu (since Linux 2.6.32) Amount of memory allocated to kernel stacks. PageTables %lu (since Linux 2.6.18) Amount of memory dedicated to the lowest level of page tables. Quicklists %lu (since Linux 2.6.27) (CONFIG_QUICKLIST is required.) [To be documented.] NFS_Unstable %lu (since Linux 2.6.18) NFS pages sent to the server, but not yet committed to stable storage. Bounce %lu (since Linux 2.6.18) Memory used for block device bounce buffers. WritebackTmp %lu (since Linux 2.6.26) Memory used by FUSE for temporary writeback buffers. CommitLimit %lu (since Linux 2.6.10) Based on the overcommit ratio (vm.overcommit_ratio), this is the total amount of memory currently available to be allocated on the system. This limit is adhered to only if strict overcommit accounting is enabled (mode 2 in /proc/sys/vm/overcommit_ratio). The CommitLimit is calculated using the following formula: CommitLimit = ([total RAM pages] - [total huge TLB pages]) * overcommit_ratio / 100 + [total swap pages] For example, on a system with 1GB of physical RAM and 7GB of swap with a overcommit_ratio of 30, this formula yields a CommitLimit of 7.3GB. For more details, see the memory overcommit documentation in the kernel source file Documentation/vm/overcommit-accounting. Committed_AS %lu The amount of memory presently allocated on the system. The committed memory is a sum of all of the memory which has been allocated by processes, even if it has not been used by them as of yet. A process which allocates 1GB of memory (using malloc(3) or similar), but touches only 300MB of that memory will show up as using only 300MB of memory even if it has the address space allocated for the entire 1GB. This 1GB is memory which has been committed to by the VM and can be used at any time by the allocating application. With strict overcommit enabled on the system (mode 2 /proc/sys/vm/overcommit_memory), allocations w»

[[ ## question ## ]]
what are high memory and low memory on linux?

Respond with the corresponding output fields, starting with the field `[[ ## reasoning ## ]]`, then `[[ ## response ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## reasoning ## ]]
High Memory and Low Memory in Linux refer to two segments of the kernel's memory space. Low Memory is the portion of memory that the kernel can access directly and is statically mapped at boot time. This area is typically used for kernel data structures and is always accessible to the kernel. High Memory, on the other hand, is not permanently mapped in the kernel's address space, meaning that the kernel cannot access it directly without first mapping it into its address space. High Memory is used for user-space applications and temporary data buffers. The distinction allows for better memory management and security, as user-space applications cannot directly access kernel-space memory.

[[ ## response ## ]]
In Linux, High Memory refers to the segment of memory that is not permanently mapped in the kernel's address space, which means the kernel must map it temporarily to access it. This area is typically used for user-space applications and temporary data buffers. Low Memory, in contrast, is the portion of memory that the kernel can access directly and is statically mapped at boot time. It is used for kernel data structures and is always accessible to the kernel. This separation enhances security by preventing user-space applications from accessing kernel-space memory directly.

[[ ## completed ## ]]


```