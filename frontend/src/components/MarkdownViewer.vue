<script setup>
import { computed } from 'vue'
import { marked } from 'marked'

const props = defineProps({
  content: {
    type: String,
    required: true
  }
})

const renderedContent = computed(() => {
  return marked.parse(props.content)
})
</script>

<template>
  <div class="markdown-viewer" v-html="renderedContent"></div>
</template>

<style scoped>
.markdown-viewer {
  line-height: 1.8;
  color: #303133;
}

.markdown-viewer :deep(h1),
.markdown-viewer :deep(h2),
.markdown-viewer :deep(h3),
.markdown-viewer :deep(h4),
.markdown-viewer :deep(h5),
.markdown-viewer :deep(h6) {
  margin-top: 24px;
  margin-bottom: 16px;
  font-weight: 600;
  line-height: 1.25;
}

.markdown-viewer :deep(h1) {
  font-size: 2em;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 0.3em;
}

.markdown-viewer :deep(h2) {
  font-size: 1.5em;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 0.3em;
}

.markdown-viewer :deep(p) {
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-viewer :deep(code) {
  background-color: rgba(27, 31, 35, 0.05);
  border-radius: 3px;
  font-size: 85%;
  margin: 0;
  padding: 0.2em 0.4em;
}

.markdown-viewer :deep(pre) {
  background-color: #282c34;
  border-radius: 6px;
  padding: 16px;
  overflow: auto;
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-viewer :deep(pre code) {
  background-color: transparent;
  border: 0;
  color: #abb2bf;
  padding: 0;
}

.markdown-viewer :deep(blockquote) {
  margin: 0;
  padding: 0 1em;
  color: #6a737d;
  border-left: 0.25em solid #dfe2e5;
}

.markdown-viewer :deep(ul),
.markdown-viewer :deep(ol) {
  padding-left: 2em;
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-viewer :deep(table) {
  border-spacing: 0;
  border-collapse: collapse;
  margin-top: 0;
  margin-bottom: 16px;
  width: 100%;
}

.markdown-viewer :deep(table th),
.markdown-viewer :deep(table td) {
  padding: 6px 13px;
  border: 1px solid #dfe2e5;
}

.markdown-viewer :deep(table tr) {
  background-color: #fff;
  border-top: 1px solid #c6cbd1;
}

.markdown-viewer :deep(table tr:nth-child(2n)) {
  background-color: #f6f8fa;
}

.markdown-viewer :deep(img) {
  max-width: 100%;
  box-sizing: content-box;
}

.markdown-viewer :deep(a) {
  color: #409eff;
  text-decoration: none;
}

.markdown-viewer :deep(a:hover) {
  text-decoration: underline;
}
</style>
