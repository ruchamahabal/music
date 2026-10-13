<template>
	<header
		class="sticky top-0 z-10 flex w-full flex-col items-center border-b border-outline-gray-2 bg-surface-base p-5 shadow-sm"
	>
		<div class="w-full">
			<div class="flex w-full items-center justify-center">
				<component
					v-if="!hideBackButton"
					:is="LucideChevronLeft"
					class="absolute left-4 h-6 w-6 cursor-pointer text-ink-gray-5 hover:text-ink-gray-8"
					@click="() => $router.back()"
				/>
				<div class="flex cursor-pointer items-center justify-center gap-2">
					<div v-if="!hideLogo && logoSVG" class="flex items-center gap-2">
						<span v-html="logoSVG" />
					</div>
					<h1 v-if="title" class="text-2xl-semibold leading-5 text-ink-gray-7">{{ title }}</h1>
				</div>

				<slot></slot>
			</div>
		</div>
	</header>
</template>

<script setup lang="ts">
import LucideChevronLeft from "~icons/lucide/chevron-left"

defineProps<{
	title?: string
	logoSVG?: string
	hideLogo?: boolean
	hideBackButton?: boolean
}>()
</script>
